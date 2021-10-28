import json


class HiScores:
    def __init__(self, filename :str="scores.json") -> None:
        self.filename: str = filename
    
    def saveScore(self, playername: str, score: int) -> None:
        scores: dict = self.getAllScores()
        scores[playername] = score
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(json.dumps(scores))

    def getAllScores(self) -> dict:
        with open(self.filename, "r", encoding="utf-8") as f:
            try:
                return json.loads(f.read())
            except json.decoder.JSONDecodeError:
                return {}

    def sort(self, values: dict) -> dict:
        _sorted: list = sorted(values.items(), key=lambda item: item[1])[::-1]
        new_dict: list = {key: value for key, value in _sorted}
        return new_dict

    def getLongestName(self, dic: dict) -> str:
        longest: str = ""
        for key in list(dic.keys()):
            if key > longest:
                longest = key
        return longest

    def generateHiScoreList(self) -> str:
        scores: dict = self.getAllScores()
        sort: dict = self.sort(scores)
        out: str = ""
        long_name: str = self.getLongestName(sort)
        for k, v in enumerate(sort.items()):
            diff_name = len(long_name) - len(v[0])
            out += str(k + 1) + " - " + str(v[0]) + " " * diff_name + " = " + str(v[1]) + "\n"
        return out

    def output(self) -> str:
        return self.generateHiScoreList()

    def __str__(self) -> str:
        return self.output()