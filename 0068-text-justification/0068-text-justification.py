class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur_line = []
        cur_word_len = 0
        for w in words:
            if cur_word_len + len(w) + len(cur_line) > maxWidth:
                total_spaces = maxWidth - cur_word_len
                gaps = len(cur_line) - 1
                if gaps == 0:
                    res.append(cur_line[0].ljust(maxWidth))
                else:
                    base_space = total_spaces // gaps
                    extra_space = total_spaces % gaps
                    line_str = ""
                    for i in range(gaps):
                        line_str += cur_line[i]
                        line_str += " "*(base_space + (1 if i < extra_space else 0))
                    line_str += cur_line[-1]
                    res.append(line_str)
                cur_line, cur_word_len = [], 0
            cur_line.append(w)
            cur_word_len += len(w)
        last_line_str = " ".join(cur_line)
        res.append(last_line_str.ljust(maxWidth))
        return res                