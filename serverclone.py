import discord
from colorama import Fore, init, Style


def print_add(message):
    print(f'{Fore.GREEN}[+]{Style.RESET_ALL} {message}')

def print_delete(message):
    print(f'{Fore.RED}[-]{Style.RESET_ALL} {message}')

def print_warning(message):
    print(f'{Fore.RED}[ATTENTION]{Style.RESET_ALL} {message}')


def print_error(message):
    print(f'{Fore.RED}[ERREUR]{Style.RESET_ALL} {message}')


class Clone:
    @staticmethod
    async def roles_delete(guild_to: discord.Guild):
            for role in guild_to.roles:
                try:
                    if role.name != "@everyone":
                        await role.delete()
                        print_delete(f"Role supprimé: {role.name}")
                except discord.Forbidden:
                    print_error(f"Erreur lors de la supprésion de ce role: {role.name}")
                except discord.HTTPException:
                    print_error(f"Impossible de supprimer ce roles: {role.name}")

    @staticmethod
    async def roles_create(guild_to: discord.Guild, guild_from: discord.Guild):
        roles = []
        role: discord.Role
        for role in guild_from.roles:
            if role.name != "@everyone":
                roles.append(role)
        roles = roles[::-1]
        for role in roles:
            try:
                await guild_to.create_role(
                    name=role.name,
                    permissions=role.permissions,
                    colour=role.colour,
                    hoist=role.hoist,
                    mentionable=role.mentionable
                )
                print_add(f"Role Crée {role.name}")
            except discord.Forbidden:
                print_error(f"Erreur lors de la création de ce role: {role.name}")
            except discord.HTTPException:
                print_error(f"Impossible de créer ce role: {role.name}")

    @staticmethod
    async def channels_delete(guild_to: discord.Guild):
        for channel in guild_to.channels:
            try:
                await channel.delete()
                print_delete(f"Salon supprimé: {channel.name}")
            except discord.Forbidden:
                print_error(f"Erreur lors de la suppresion de ce salon: {channel.name}")
            except discord.HTTPException:
                print_error(f"Impossible de supprimer ce salon: {channel.name}")

    @staticmethod
    async def categories_create(guild_to: discord.Guild, guild_from: discord.Guild):
        channels = guild_from.categories
        channel: discord.CategoryChannel
        new_channel: discord.CategoryChannel
        for channel in channels:
            try:
                overwrites_to = {}
                for key, value in channel.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    overwrites_to[role] = value
                new_channel = await guild_to.create_category(
                    name=channel.name,
                    overwrites=overwrites_to)
                await new_channel.edit(position=channel.position)
                print_add(f"Catégorie Crée: {channel.name}")
            except discord.Forbidden:
                print_error(f"Impossible de supprimer cette catégorie: {channel.name}")
            except discord.HTTPException:
                print_error(f"Impossible de supprimer cette catégorie: {channel.name}")

    @staticmethod
    async def channels_create(guild_to: discord.Guild, guild_from: discord.Guild):
        channel_text: discord.TextChannel
        channel_voice: discord.VoiceChannel
        category = None
        for channel_text in guild_from.text_channels:
            try:
                for category in guild_to.categories:
                    try:
                        if category.name == channel_text.category.name:
                            break
                    except AttributeError:
                        print_warning(f"Le salon {channel_text.name} n'a pas de catégorie !")
                        category = None
                        break

                overwrites_to = {}
                for key, value in channel_text.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    overwrites_to[role] = value
                try:
                    new_channel = await guild_to.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position,
                        topic=channel_text.topic,
                        slowmode_delay=channel_text.slowmode_delay,
                        nsfw=channel_text.nsfw)
                except:
                    new_channel = await guild_to.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position)
                if category is not None:
                    await new_channel.edit(category=category)
                print_add(f"Salon crée: {channel_text.name}")
            except discord.Forbidden:
                print_error(f"Erreur quand la création de se salon s'est faite: {channel_text.name}")
            except discord.HTTPException:
                print_error(f"Impossible de créer ce salon textuel: {channel_text.name}")
            except:
                print_error(f"Impossible de créer ce salon textuel: {channel_text.name}")

        category = None
        for channel_voice in guild_from.voice_channels:
            try:
                for category in guild_to.categories:
                    try:
                        if category.name == channel_voice.category.name:
                            break
                    except AttributeError:
                        print_warning(f"Le salon {channel_voice.name} n'a pas de catégorie !")
                        category = None
                        break

                overwrites_to = {}
                for key, value in channel_voice.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    overwrites_to[role] = value
                try:
                    new_channel = await guild_to.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position,
                        bitrate=channel_voice.bitrate,
                        user_limit=channel_voice.user_limit,
                        )
                except:
                    new_channel = await guild_to.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position)
                if category is not None:
                    await new_channel.edit(category=category)
                print_add(f"Salon Vocal Crée: {channel_voice.name}")
            except discord.Forbidden:
                print_error(f"Impossible de créer ce salon vocal: {channel_voice.name}")
            except discord.HTTPException:
                print_error(f"Impossible de créer ce salon vocal: {channel_voice.name}")
            except:
                print_error(f"Impossible de créer ce salon vocal: {channel_voice.name}")


    @staticmethod
    async def emojis_delete(guild_to: discord.Guild):
        for emoji in guild_to.emojis:
            try:
                await emoji.delete()
                print_delete(f"Emoji Supprimé: {emoji.name}")
            except discord.Forbidden:
                print_error(f"Impossible de supprimer cette émoji{emoji.name}")
            except discord.HTTPException:
                print_error(f"Impossible de supprimer cette émoji {emoji.name}")

    @staticmethod
    async def emojis_create(guild_to: discord.Guild, guild_from: discord.Guild):
        emoji: discord.Emoji
        for emoji in guild_from.emojis:
            try:
                emoji_image = await emoji.url.read()
                await guild_to.create_custom_emoji(
                    name=emoji.name,
                    image=emoji_image)
                print_add(f"Emoji Crée {emoji.name}")
            except discord.Forbidden:
                print_error(f"Erreur a la création de cette émoji {emoji.name} ")
            except discord.HTTPException:
                print_error(f"Erreur a la création de cette émoji {emoji.name}")

    @staticmethod
    async def guild_edit(guild_to: discord.Guild, guild_from: discord.Guild):
        try:
            try:
                icon_image = await guild_from.icon_url.read()
            except discord.errors.DiscordException:
                print_error(f"N'arrive pas a mettre le logo de ce serveur {guild_from.name}")
                icon_image = None
            await guild_to.edit(name=f'{guild_from.name}')
            if icon_image is not None:
                try:
                    await guild_to.edit(icon=icon_image)
                    print_add(f"Logo du serveur changé: {guild_to.name}")
                except:
                    print_error(f"Erreur lors du changement du logo du serveur: {guild_to.name}")
        except discord.Forbidden:
            print_error(f"Erreur lors du changement du logo du serveur: {guild_to.name}")