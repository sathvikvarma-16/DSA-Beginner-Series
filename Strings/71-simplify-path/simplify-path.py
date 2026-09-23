class Solution:
    def simplifyPath(self, path: str) -> str:

        result = []

        folders = path.split("/")

        for folder in folders:

            if folder == "" or folder == ".":
                continue

            elif folder == "..":

                if result:
                    result.pop()

            else:
                result.append(folder)

        return "/" + "/".join(result)