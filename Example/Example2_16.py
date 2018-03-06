import UserList


class AutoList(UserList.UserList):

    def __setitem__(self, key, value):
        if key == len(self.data):
            self.data.append(value)
        else:
            self.data[key] = value


a_list = AutoList()

for i in range(10):
    a_list[i] = i

a_list[10] = 10

print a_list
