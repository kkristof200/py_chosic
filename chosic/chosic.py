# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional, List, Union, Dict

# Pip
from ksimpleapi import Api
from bs4 import BeautifulSoup as bs

# Local
from .enums.mood import Mood
from .enums.genre import Genre

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------ class: Chosic ------------------------------------------------------------- #

class Chosic(Api):

    # -------------------------------------------------------- Public methods -------------------------------------------------------- #

    def get_titles(
        self,
        mood: Optional[Union[Mood, int]] = None,
        genre: Optional[Union[Genre, int]] = None,
        user_agent: Optional[Union[str, List[str]]] = None,
        proxy: Optional[Union[str, List[str]]] = None,
        max_request_try_count: Optional[int] = None,
        sleep_s_between_failed_requests: Optional[float] = None,
        debug: Optional[bool] = None
    ) -> Optional[List[str]]:
        debug = debug if debug is not None else self._request.debug
        url = 'https://www.chosic.com/song-name-generator-by-genre-and-mood/'
        mood = mood or Mood.All
        genre = genre or Genre.All

        if type(mood) == Mood:
            mood = mood.value

        if type(genre) == Genre:
            genre = genre.value

        try:
            res = self._post(
                url,
                body={
                    'mood': mood,
                    'genre': genre
                },
                proxy=proxy,
                user_agent=user_agent,
                max_request_try_count=max_request_try_count,
                sleep_s_between_failed_requests=sleep_s_between_failed_requests,
                debug=debug
            )
            soup = bs(res.content, 'lxml')

            return [e.text.replace('Search Spotify', '').strip().title() for e in soup.find_all('div', class_='name')]
        except Exception as e:
            if debug:
                print(e)

            return None

    @classmethod
    def get_titles_cls(
        cls,
        mood: Optional[Union[Mood, int]] = None,
        genre: Optional[Union[Genre, int]] = None,
        user_agent: Optional[Union[str, List[str]]] = None,
        proxy: Optional[Union[str, List[str]]] = None,
        max_request_try_count: Optional[int] = None,
        sleep_s_between_failed_requests: Optional[float] = None,
        debug: Optional[bool] = None
    ) -> Optional[List[str]]:
        return Chosic().get_titles(
            mood=mood,
            genre=genre,
            user_agent=user_agent,
            proxy=proxy,
            max_request_try_count=max_request_try_count,
            sleep_s_between_failed_requests=sleep_s_between_failed_requests,
            debug=debug            
        )

    @classmethod
    def extra_headers(self) -> Optional[Dict[str, any]]:
        return {
            'Accept-Encoding': 'gzip, deflate'
        }


# ---------------------------------------------------------------------------------------------------------------------------------------- #