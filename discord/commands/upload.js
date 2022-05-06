const { SlashCommandBuilder } = require('discord.js');
const fetch = require('node-fetch');

module.exports = {
	data: new SlashCommandBuilder()
        .setName('upload')
        .setDescription('Upload an image.')
        .addAttachmentOption(option =>
            option.setName('image')
                .setDescription('Image to upload.')
                .setRequired(true)),
    async execute(interaction) 
        const image = interaction.options.getAttachment('image');
        const file = await image.getFile();
        const data = await file.read();
        const buffer = Buffer.from(data);
        const encoded = buffer.toString('base64');



        console.log(typeof (image));
    },
};