class File:
    file_name : str
    file_type : str 
    def __init__(self,file_name,file_type):
        self.file_name=file_name
        self.file_type=file_type
    #change file_name method
    def change_name(self,new_name):
        self.file_name=new_name


class Directory:
    dir_name : str
    dir_content : list 
    def __init__(self, dir_name,dir_content):
        self.dir_name=dir_name
        self.dir_content=dir_content

    #methods like search, delete, list, create

    #creating a file
    def file_create(self, file_name,file_type):
        created_file=File(file_name,file_type)
        self.dir_content.append(created_file)

    #creating a dir
    def dir_create(self, dir_name):
        self.dir_content.append(Directory(dir_name, []))

    #search
    def search(self, name):
        n=len(self.dir_content)
        i=0
        found =False

        def helper(dir_content, n, i):
            nonlocal found
            if(i==n or found):
                return

            child = dir_content[i]

            if isinstance(child, File):
                if(child.file_name == name or child.file_name + "." + child.file_type == name):
                    found=True
                    return

            if isinstance(child, Directory):
                if(child.dir_name == name):
                    found=True
                    return
                helper(child.dir_content, len(child.dir_content), 0)

            helper(dir_content, n , i+1)

        helper(self.dir_content,n, 0)
        if(found):
            return True
        return False

    def delete(self, name):
        n=len(self.dir_content)
        i=0
        found =False

        def helper(dir_content, n, i):
            nonlocal found
            if(i==n or found==True):
                return

            child = dir_content[i]

            if isinstance(child, File):
                if(child.file_name == name or child.file_name + "." + child.file_type == name):
                    found=True
                    dir_content.remove(child)
                    return

            if isinstance(child, Directory):
                if(child.dir_name == name):
                    found=True
                    dir_content.remove(child)
                    return
                helper(child.dir_content, len(child.dir_content), 0)

            helper(dir_content, n , i+1)

        helper(self.dir_content,n, 0)
        if(found):
            return "deleted"
        else:
            return "not found"

    def list(self):
        output=[]
        n=len(self.dir_content)
        i=0

        while(i<n):
            child=self.dir_content[i]

            if isinstance(child, File):
                output.append(child.file_name + "." + child.file_type)

            if isinstance(child, Directory):
                output.append(child.dir_name)

            i=i+1

        return output


class FileSystem:
    def __init__(self):
        self.root=Directory("root",[])

    def file_create(self, file_name,file_type):
        self.root.file_create(file_name,file_type)

    def dir_create(self, dir_name):
        self.root.dir_create(dir_name)

    def search(self, name):
        return self.root.search(name)

    def delete(self, name):
        return self.root.delete(name)

    def list(self):
        return self.root.list()