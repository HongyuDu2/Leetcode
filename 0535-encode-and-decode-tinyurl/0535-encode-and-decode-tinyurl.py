class Codec:
    def __init__(self):
        self.url_map = {} # 存放 ID -> LongURL
        self.count = 0    # 自增计数器
        self.base_url = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """将长网址转换为短网址"""
        self.count += 1
        key = str(self.count)
        self.url_map[key] = longUrl
        return self.base_url + key

    def decode(self, shortUrl: str) -> str:
        """将短网址还原为长网址"""
        # 提取短网址最后的那个 key
        key = shortUrl.replace(self.base_url, "")
        return self.url_map[key]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))