const { SlashCommandBuilder } = require('@discordjs/builders');
const fetch = require('node-fetch');

module.exports = {
	data: new SlashCommandBuilder()
        .setName('domain')
        .setDescription('Change the current domain you\'re using.')
        .addStringOption(option =>
            option.setName('newdomain')
                .setDescription('The domain to change to.')
                .setRequired(true)),
    async execute(interaction) {
        const newDomain = interaction.options.getString('newdomain');
        await fetch('http://127.0.0.1:5000/domain', {
            method: 'PUT',
            headers:{          
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: interaction.user.id,
                domain: newDomain
            })
        }).then(response => response.json()).then(data => {res = data;});

        if (res.message === 'Updated') {
            await interaction.reply(`Domain changed to: ${newDomain}`);
            
        } else {
            await interaction.reply('There was an error while changing your domain.');
        }
        
    },
};