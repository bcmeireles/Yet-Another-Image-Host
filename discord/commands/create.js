const { SlashCommandBuilder } = require('discord.js');
const fetch = require('node-fetch');

module.exports = {
	data: new SlashCommandBuilder()
        .setName('create')
        .setDescription('Create an account.'),
    async execute(interaction) {
        await fetch('http://127.0.0.1:5000/domains').then(response => response.json()).then(data => {res = data;});
        const array = res.domains;

        const newDomain = array[array.length * Math.random() | 0];
        const newKey = 'YAIH-' + Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);

        console.log(newDomain);
        console.log(newKey);

        await fetch('http://127.0.0.1:5000/user', {
            method: 'POST',
            headers:{          
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: interaction.user.id,
                domain: newDomain,
                key: newKey
            })
        }).then(response => response.json()).then(data => {res = data;});

        console.log(res);

        
        interaction.reply(`Your account has been created: ${newDomain} ${newKey}`);
    },
};