from requests import get
def main():
    url="https://randomuser.me/api"
    print(get(url))

if __name__=='__main__':
    print('random users')
    main()