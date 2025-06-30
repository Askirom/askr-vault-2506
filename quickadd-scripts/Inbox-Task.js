const task = await inputPrompt("Task:");
const taskLine = `- [ ] ${task} 📅 ${new Date().toISOString().split('T')[0]}`;
await app.vault.append("00 To Sort/Inbox - Tasks.md", taskLine + "\n");
