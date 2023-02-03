import typing as tp

from dto.token import TokenPairDTO, UpdateTokenDTO


class TokenMapper:
    @staticmethod
    def convert_to_token_pair_dto(data: tp.Tuple[str, str]) -> TokenPairDTO:
        return TokenPairDTO(*data)

    @staticmethod
    def convert_to_update_token_dto(
        user_id: int, access_token: str, refresh_token: str
    ):
        return UpdateTokenDTO(user_id, access_token, refresh_token)
