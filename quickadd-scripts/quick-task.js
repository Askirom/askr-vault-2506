module.exports = async (params) => {
    const { quickAddApi: { inputPrompt, suggester } } = params;
    
    // Get task description
    const task = await inputPrompt("Task:");
    if (!task) return;
    
    // Client detection patterns
    const clients = ["EMPIC", "RCG", "SECUD", "FITS", "FDFRI", "EHFREI", "CLIFO", "EKIBA", "GOSME", "INSTO", "VEDES", "VGALT"];
    const detectedClient = clients.find(client => 
        task.toUpperCase().includes(client) || 
        task.toUpperCase().includes(`@${client.toLowerCase()}`)
    );
    
    // Network keywords
    const networkKeywords = ["BvD", "Maibaum", "Nürnberg", "Prüfaufgaben"];
    const isNetwork = networkKeywords.some(keyword => 
        task.toUpperCase().includes(keyword.toUpperCase())
    );
    
    // Personal keywords
    const personalKeywords = ["personal", "private", "learn", "study", "health", "fitness"];
    const isPersonal = personalKeywords.some(keyword => 
        task.toLowerCase().includes(keyword.toLowerCase())
    );
    
    // Route to appropriate location
    let targetFile, insertAfter;
    
    if (detectedClient) {
        targetFile = `20 Quests/PROFESSIONAL/${detectedClient}/QUEST - ${detectedClient}.md`;
        insertAfter = "## Action Log & Tasks";
    } else if (isNetwork) {
        if (task.toUpperCase().includes("BVD")) {
            targetFile = "20 Quests/NETWORK/BvD RG Nürnberg/QUEST - BvD RG Nürnberg.md";
        } else {
            targetFile = "20 Quests/NETWORK/Maibaum/QUEST - Maibaum.md";
        }
        insertAfter = "## Action Log & Tasks";
    } else if (isPersonal) {
        targetFile = "20 Quests/PERSONAL/QUEST - Personal.md";
        insertAfter = "## Action Log & Tasks";
    } else {
        // Default to today's daily note
        const today = new Date().toISOString().split('T')[0];
        targetFile = `01 Daily/${today}.md`;
        insertAfter = "## Professional Log";
    }
    
    // Get due date (optional)
    const dueDate = await inputPrompt("Due date (YYYY-MM-DD, or leave empty):");
    const dueDateStr = dueDate ? ` 📅 ${dueDate}` : ` 📅 ${new Date().toISOString().split('T')[0]}`;
    
    // Get contact (optional)
    const contact = await inputPrompt("Contact (@person, or leave empty):");
    const contactStr = contact ? ` ${contact.startsWith('@') ? contact : '@' + contact}` : '';
    
    // Format task
    const taskLine = `- [ ] ${task}${contactStr}${dueDateStr}`;
    
    // Insert into target file
    const file = app.vault.getAbstractFileByPath(targetFile);
    if (file) {
        const content = await app.vault.read(file);
        const lines = content.split('\n');
        const insertIndex = lines.findIndex(line => line.includes(insertAfter));
        
        if (insertIndex !== -1) {
            lines.splice(insertIndex + 1, 0, taskLine);
            await app.vault.modify(file, lines.join('\n'));
        } else {
            // Fallback: append to end
            await app.vault.modify(file, content + '\n' + taskLine);
        }
    } else {
        // Create file if it doesn't exist (for daily notes)
        if (targetFile.includes('01 Daily/')) {
            const template = await app.vault.read(app.vault.getAbstractFileByPath('10 Library/TEMPLATES/Template Daily Log.md'));
            const today = new Date().toISOString().split('T')[0];
            const dailyContent = template.replace(/{{date:YYYY-MM-DD}}/g, today);
            await app.vault.create(targetFile, dailyContent);
            
            // Now insert the task
            const newFile = app.vault.getAbstractFileByPath(targetFile);
            const content = await app.vault.read(newFile);
            const lines = content.split('\n');
            const insertIndex = lines.findIndex(line => line.includes(insertAfter));
            lines.splice(insertIndex + 1, 0, taskLine);
            await app.vault.modify(newFile, lines.join('\n'));
        }
    }
    
    new Notice(`Task added to ${targetFile}`);
};