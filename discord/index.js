const fs = require('node:fs');
const { Client, Collection, Intents } = require('discord.js');
const { token } = require('./config.json');

const client = new Client({ intents: [Intents.FLAGS.GUILDS] });

client.commands = new Collection();
const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));

for (const file of commandFiles) {
	const command = require(`./commands/${file}`);
	client.commands.set(command.data.name, command);
}

client.once('ready', c => {
	console.log(`Ready! Logged in as ${c.user.tag}`);
});

client.on('interactionCreate', async interaction => {
    console.log(`${interaction.user.tag} in #${interaction.channel.name} triggered an interaction.`);

	if (!interaction.isCommand()) return;

	const { commandName } = interaction;

	const command = client.commands.get(interaction.commandName);

	if (!command) return;

	try {
		await command.execute(interaction);
	} catch (error) {
		console.error(error);
		if (commandName === 'info') {
			await interaction.reply('There was an error while executing this command! Do you have an account already?');
		
		} else {
			await interaction.reply({ content: 'There was an error while executing this command!', ephemeral: true });
		}
}});

client.login(token);