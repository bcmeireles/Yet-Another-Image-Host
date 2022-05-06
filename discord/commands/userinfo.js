const { SlashCommandBuilder } = require('discord.js');
const fetch = require('node-fetch');

module.exports = {
	data: new SlashCommandBuilder()
        .setName('info')
        .setDescription('Get your account info (or create one if your do not have one already).'),
    async execute(interaction) {
        await fetch(`http://127.0.0.1:5000/user?id=${interaction.user.id}`).then(response => response.json()).then(data => {res = data;});
        interaction.reply(`Your account info: ${res.domain} ${res.key}`);
    },
};