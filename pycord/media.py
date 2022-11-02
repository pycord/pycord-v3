# -*- coding: utf-8 -*-
# cython: language_level=3
# Copyright (c) 2021-present VincentRPS
# Copyright (c) 2022-present Pycord Development
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE
from __future__ import annotations

from typing import TYPE_CHECKING

from .enums import StickerFormatType, StickerType
from .role import Role
from .snowflake import Snowflake
from .types import (
    Attachment as DiscordAttachment,
    Emoji as DiscordEmoji,
    Sticker as DiscordSticker,
    StickerItem as DiscordStickerItem,
    User as DiscordUser,
)
from .user import User
from .utils import UNDEFINED, UndefinedType

if TYPE_CHECKING:
    from .state import State


class Emoji:
    def __init__(self, data: DiscordEmoji, state: State) -> None:
        self.id: Snowflake | None = Snowflake(data['id']) if data['id'] is not None else None
        self.name: str | None = Snowflake(data['name']) if data['name'] is not None else None
        self._roles: list[Snowflake] = [Snowflake(iden) for iden in data.get('roles', [])]
        self.roles: list[Role] = []
        self._user: DiscordUser | UndefinedType = data.get('user', UNDEFINED)
        self.user: UndefinedType | User = User(self._user, state) if self._user is not UNDEFINED else UNDEFINED
        self.require_colons: UndefinedType | bool = data.get('require_colons', UNDEFINED)
        self.managed: UndefinedType | bool = data.get('managed', UNDEFINED)
        self.animated: UndefinedType | bool = data.get('animated', UNDEFINED)
        self.available: UndefinedType | bool = data.get('availabke', UNDEFINED)

    def _inject_roles(self, roles: list[Role]) -> None:
        for role in roles:
            if role.id in self._roles:
                self.roles.append(role)


class StickerItem:
    def __init__(self, data: DiscordStickerItem) -> None:
        self.id: Snowflake = Snowflake(data['id'])
        self.name: str = data['name']
        self.format_type: StickerFormatType = StickerFormatType(data['format_type'])


class Sticker:
    def __init__(self, data: DiscordSticker, state: State) -> None:
        self.id: Snowflake | None = Snowflake(data['id'])
        self.pack_id: Snowflake | None = Snowflake(data['pack_id']) if data['pack_id'] is not None else None
        self.name: str = data['name']
        self.description: str | None = data['description']
        self.tags: list[str] = data['tags'].split(',')
        self.type: StickerType = StickerType(data['type'])
        self.format_type: StickerFormatType = StickerFormatType(data['format_type'])
        self.available: bool | UndefinedType = data.get('available', UNDEFINED)
        self.guild_id: Snowflake | None = Snowflake(data['guild_id']) if data['guild_id'] is not None else None
        self._user: DiscordUser | UndefinedType = data.get('user', UNDEFINED)
        self.user: UndefinedType | User = User(self._user, state) if self._user is not UNDEFINED else UNDEFINED
        self.sort_value: UndefinedType | int = data.get('sort_value', UNDEFINED)


class Attachment:
    def __init__(self, data: DiscordAttachment, state: State) -> None:
        self.id: Snowflake = Snowflake(data['id'])
        self.filename: str = data['filename']
        self.description: str | UndefinedType = data.get('description', UNDEFINED)
        self.content_type: str | UndefinedType = data.get('content_type', UNDEFINED)
        self.size: int = data.get('size')
        self.url: str = data.get('url')
        self.proxy_url: str = data.get('proxy_url')
        self.height: int | None | UndefinedType = data.get('height', UNDEFINED)
        self.width: int | None | UndefinedType = data.get('width', UNDEFINED)
        self.ephemeral: bool | UndefinedType = data.get('ephemeral', UNDEFINED)