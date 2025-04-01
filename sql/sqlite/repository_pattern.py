from dataclasses import dataclass
import sqlite3


@dataclass
class Show:
    name: str
    description: str
    anime_status: str
    status: str
    season: int = 1
    episodes: int = None
    episodes_watched: int = 0
    comments: str | None = None
    start_from: int = 0


class ExampleSQLiteRepository:
    def __init__(self, connection_string, **kwargs):
        # initialize database connection
        self._connection_string = connection_string
        self._connection = sqlite3.connect(connection_string, **kwargs)

        # Initialise database tables as well here if needed
        # CREATE IF NOT EXISTS ... etc

    def create(self, item: Show) -> None:
        with self._connection as con:
            con.execute(
                'INSERT INTO "show-tracker" (name, season, episodes, eps_watched, description, comments, anime_status, status, start_from) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (
                    item.name,
                    item.season,
                    item.episodes,
                    item.episodes_watched,
                    item.description,
                    item.comments,
                    item.anime_status,
                    item.status,
                    item.start_from,
                ),
            )

    def get_all(self) -> list[Show]:
        with self._connection as con:
            shows = con.execute('SELECT * FROM "show-tracker"').fetchall()

        return [
            Show(
                name=show[0],
                season=show[1],
                episodes=show[2],
                episodes_watched=show[3],
                description=show[4],
                comments=show[5],
                anime_status=show[6],
                status=show[7],
                start_from=show[8],
            )
            for show in shows
        ]

    def get_by_name(self, name) -> Show:
        with self._connection as con:
            show = con.execute(
                'SELECT * FROM "show-tracker" WHERE name = ?', (name,)
            ).fetchone()

        return Show(
            name=show[0],
            season=show[1],
            episodes=show[2],
            episodes_watched=show[3],
            description=show[4],
            comments=show[5],
            anime_status=show[6],
            status=show[7],
            start_from=show[8],
        )

    def get_by_status(self, status="watching", sort_by_name=False) -> list[Show]:
        with self._connection as con:
            if sort_by_name:
                query = 'SELECT * FROM "show-tracker" WHERE status = ? ORDER BY name'
            else:
                query = 'SELECT * FROM "show-tracker" WHERE status = ?'
            shows = con.execute(
                query, (status,)
            ).fetchall()

        return [
            Show(
                name=show[0],
                season=show[1],
                episodes=show[2],
                episodes_watched=show[3],
                description=show[4],
                comments=show[5],
                anime_status=show[6],
                status=show[7],
                start_from=show[8],
            )
            for show in shows
        ]

    def update(self, item: Show) -> None:
        """
        Update whole row, does not update name of show
        """
        with self._connection as con:
            con.execute(
                """UPDATE "show-tracker"
                SET
                season = ?,
                episodes = ?,
                eps_watched = ?,
                description = ?,
                comments = ?,
                anime_status = ?,
                status = ?
                WHERE
                name = ?
                """,
                (
                    item.season,
                    item.episodes,
                    item.episodes_watched,
                    item.description,
                    item.comments,
                    item.anime_status,
                    item.status,
                    item.name,
                ),
            )

    def close(self):
        self._connection.close()
