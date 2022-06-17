from typing import List


class Quiz:
    type: str = 'quiz'

    def __init__(self, quiz_id, qeustions, options, corect_opustions_id, owner_id) -> None:
        self.quiz_id: str = quiz_id
        self.qeustions: str = qeustions
        self.options: List[str] = [*options]
        self.corect_options_id: int = corect_opustions_id
        self.owner_id: int = owner_id
        self.winners: List[int]
        self.chat_id: int = 0
        self.masseg_id: int = 0
