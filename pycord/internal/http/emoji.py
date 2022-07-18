# Copyright (c) 2021-2022 VincentRPS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from discord_typings import EmojiData, Snowflake

from pycord.internal.http.route import Route
from pycord.mixins import RouteCategoryMixin
from pycord.utils import _convert_base64_from_bytes


class EmojiRoutes(RouteCategoryMixin):
    async def list_guild_emojis(self, guild_id: Snowflake) -> EmojiData:
        return await self.request("GET", Route("/guilds/{guild_id}/emojis", guild_id=guild_id))

    async def get_guild_emoji(self, guild_id: Snowflake, emoji_id: Snowflake) -> EmojiData:
        return await self.request("GET",
                                  Route("/guilds/{guild_id}/emojis/{emoji_id}", guild_id=guild_id, emoji_id=emoji_id))

    async def create_guild_emoji(
        self,
        guild_id: Snowflake,
        *,
        name: str,
        image: bytes,
        roles: list[Snowflake] | None = None,
        reason: str | None = None,
    ) -> EmojiData:
        payload = {
            "name": name,
            "image": _convert_base64_from_bytes(image),
            "roles": roles or [],
        }

        return await self.request("POST", Route("/guilds/{guild_id}/emojis", guild_id=guild_id), payload, reason=reason)

    async def modify_guild_emoji(
        self,
        guild_id: Snowflake,
        emoji_id: Snowflake,
        *,
        name: str = ...,
        roles: list[Snowflake] | None = ...,
        reason: str | None = None,
    ) -> EmojiData:
        payload = {}
        if name is not ...:
            payload["name"] = name
        if roles is not ...:
            payload["roles"] = roles or []

        return await self.request(
            "PATCH",
            Route("/guilds/{guild_id}/emojis/{emoji_id}", guild_id=guild_id, emoji_id=emoji_id),
            payload,
            reason=reason
        )

    async def delete_guild_emoji(self, guild_id: Snowflake, emoji_id: Snowflake, *, reason: str | None = None) -> None:
        return await self.request("DELETE",
                                  Route("/guilds/{guild_id}/emojis/{emoji_id}", guild_id=guild_id, emoji_id=emoji_id),
                                  reason=reason)
