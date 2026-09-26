class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        key_map = {k:v for k,v in knowledge}
        output = []
        current_key = []
        in_bracket = False
        for char in s:
            if char == "(":
                in_bracket = True
            elif char == ")":
                in_bracket = False
                key_str = "".join(current_key)
                translate = key_map.get(key_str,"?")
                output.append(translate)
                current_key = []
            else:
                if in_bracket:
                    current_key.append(char)
                else:
                    output.append(char)
        return "".join(output)