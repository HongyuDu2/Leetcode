class Solution(object):
    def simplifyPath(self, path):

        path_list = list(path)

        def is_only_dots(s):
            return all(char == '.' for char in s) and len(s) > 0

        if path_list[0] != '/':
            path_list.insert(0, '/')

        if path_list[-1] == '/':
            path_list.pop()

        for i in range(0, len(path_list)-1):
            if path_list[i] == '/':
                for j in range(i+1, len(path_list)-1):
                    if path_list[j] == '/':
                        path_list[j] = '&'
                    else:
                        break
        while '&' in path_list:
            path_list.remove('&')

        path_list = ''.join(path_list)
        path_list = path_list.split('/')

        for i in range(len(path_list)):
            if path_list[i] == '..' and i != 1:
                for j in range(i-1, -1, -1):
                    if is_only_dots(path_list[j]) or path_list[j] == '&' or  path_list[j] == '':
                        continue
                    else: 
                        path_list[j] = '&'
                        break

        while '&' in path_list:
            path_list.remove('&')
        while '.' in path_list:
            path_list.remove('.')
        while '..' in path_list:
            path_list.remove('..')

        if path_list[-1] == '' and len(path_list) > 1:
            path_list.pop()

        if path_list[-1] == '' and len(path_list) > 1:
            path_list.pop()



        if len(path_list) == 1 and path_list[0] == '':
            result = '/'
        else:
            result = '/'.join(path_list)
        
        
        return result

        
        """
        :type path: str
        :rtype: str
        """