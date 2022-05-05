const { SlashCommandBuilder } = require('@discordjs/builders');
const fetch = require('node-fetch');

module.exports = {
	data: new SlashCommandBuilder()
        .setName('key')
        .setDescription('Generate a new key for your account.'),
    async execute(interaction) {
        const newKey = 'YAIH-' + Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
        
        await fetch('http://127.0.0.1:5000/key', {
            method: 'PUT',
            headers:{          
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: interaction.user.id,
                key: newKey
            })
        }).then(response => response.json()).then(data => {res = data;});

        if (res.message === 'Updated') {
            interaction.reply(`Your new key: ${newKey}`);
        } else {
            interaction.reply('There was an error while generating a new key.');
        }
    },
};