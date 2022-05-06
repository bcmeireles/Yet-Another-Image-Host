const { SlashCommandBuilder } = require('discord.js');
const { EmbedBuilder } = require('discord.js');

const fetch = require('node-fetch');

module.exports = {
	data: new SlashCommandBuilder()
        .setName('domains')
        .setDescription('Sends the list of domains available on the host.'),
    async execute(interaction) {
        await fetch('http://127.0.0.1:5000/domains').then(response => response.json()).then(data => {res = data;});
        
        const array = res.domains;

        const exampleEmbed = new EmbedBuilder()
            .setColor('#ffffff')
            .setTitle('Yet Another Image Host')
            .setURL('https://github.com/dvntx/Yet-Another-Image-Host')
            .setAuthor({ name: 'dvntx', iconURL: 'https://avatars.githubusercontent.com/u/67381633', url: 'https://github.com/dvntx' })
            .setTimestamp()
            .setFooter({ text: 'yaih', iconURL: 'https://avatars.githubusercontent.com/u/67381633' });

        
            
        await interaction.reply({ embeds: [exampleEmbed] })
    },
};