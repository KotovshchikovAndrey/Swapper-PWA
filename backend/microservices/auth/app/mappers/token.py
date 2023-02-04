import typing as tp

from dto.token import TokenPairDTO, TokenUpdateDTO


class TokenMapper:
    @staticmethod
    def convert_to_token_pair_dto(data: tp.Tuple[str, str]) -> TokenPairDTO:
        return TokenPairDTO(*data)

    @staticmethod
    def convert_to_update_dto(
        user_id: int, access_token: str, refresh_token: str
    ) -> TokenUpdateDTO:
        return TokenUpdateDTO(user_id, access_token, refresh_token)
