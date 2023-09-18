"""Discord network communication logic"""

import asyncio
from typing import BinaryIO, Sequence, Optional, Union

import aiohttp

from .classes import (
    DSnowflake,
    DEmbed,
    DAllowedMentions,
    DMessageReference,
    DComponent,
    DAttachment
)


class DSession:
    """Discord connection session object, contains the API interaction logic"""
    BASE_URL = "https://discord.com/api/v10"

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        connector: Optional[aiohttp.TCPConnector] = None
    ) -> None:
        self.connector: Optional[aiohttp.TCPConnector] = connector
        self.loop: asyncio.AbstractEventLoop = loop
        self.session = None

    ### Discord actions
    def send_message(
        self,
        channel: Union[int, DSnowflake],
        *,
        content: Optional[str] = None,
        nonce: Optional[Union[int, str]] = None,
        tts: bool = False,
        embeds: Optional[Sequence[DEmbed]] = None,
        allowed_mentions: Optional[DAllowedMentions] = None,
        message_reference: Optional[DMessageReference] = None,
        components: Optional[Sequence[DComponent]] = None,
        sticker_ids: Optional[Sequence[Union[int, DSnowflake]]] = None,
        files: Optional[Sequence[Union[BinaryIO, bytes]]] = None,
        payload_json: Optional[str] = None,
        attachments: Optional[Sequence[DAttachment]] = None,
        flags: Optional[int] = None
    ):
        """Send a message object to a Discord.

        :param channel: An id or a Snowflake object of the channel to post the message to.
        :type channel: Union[int, DSnowflake]
        :param content: Text content of the message (up to 2000 characters), defaults to None
        :type content: Optional[str], optional
        :param nonce: A value for verifying whether the message was sent successfully,
        defaults to None
        :type nonce: Optional[Union[int, str]], optional
        :param tts: Whether or not to use the TTS feature for the message, defaults to False
        :type tts: bool, optional
        :param embeds: List of embeds to be sent with the message, defaults to None
        :type embeds: Optional[Sequence[DEmbed]], optional
        :param allowed_mentions: Which mentions are allowed in the message, defaults to None
        :type allowed_mentions: Optional[DAllowedMentions], optional
        :param message_reference: Reference to the message to which the response is being sent,
        if any, defaults to None
        :type message_reference: Optional[DMessageReference], optional
        :param components: List of message components such as buttons, defaults to None
        :type components: Optional[Sequence[DComponent]], optional
        :param sticker_ids: Up to three stickers to send with the message, defaults to None
        :type sticker_ids: Optional[Sequence[Union[int, DSnowflake]]], optional
        :param files: Contents of the files being sent, defaults to None
        :type files: Optional[Sequence[Union[BinaryIO, bytes]]], optional
        :param payload_json: JSON-encoded body of non-file params when uploading files,
        defaults to None
        :type payload_json: Optional[str], optional
        :param attachments: Attachment objects with filename and description,
        defaults to None
        :type attachments: Optional[Sequence[DAttachment]], optional
        :param flags: Message flags combined as a bitfield
        (SUPPRESS_EMBEDS and SUPPRESS_NOTIFICATIONS), defaults to None
        :type flags: Optional[int], optional
        """

        return  # TODO: literally everything
