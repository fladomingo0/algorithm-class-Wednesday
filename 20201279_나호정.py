class Node:
    def __init__(self,elem, next=None):
        self.data = elem 
        self.link = next 

    def append(self, new) : 
        if new is not None:
            new.link = self.link 
            self.link = new      

    def popNext(self): 
        deleted_node = self.link
        if deleted_node is not None: 
            self.link = deleted_node.link
        return deleted_node

# 단순연결리스트 클래스
class LinkedList:
    def __init__(self):
        self.head = None # 비어있는 리스트의 초기 상태

    # 주요 기본 연산
    def isEmpty(self):
        # 리스트의 빈 상태 검사
        return self.head == None
    
    def isFull(self):
        # 리스트의 포화 상태 검사
        return False # 동적 노드 할당
    
    def getNode(self, pos): # pos 기반 연산
        # pos 위치에 있는 노드를 반환 
        # pos는 리스트의 인덱스 0부터 고려
        if pos < 0 : return None # pos는 유효하지않은 위치
        if self.head == None: # 리스트가 빈 상태 
            return None
        else :
            ptr = self.head
            for _ in range(pos):
                if ptr == None : # pos가 리스트보다 크기가 큰 경우(유효하지 않는 위치)
                    return None
                ptr = ptr.link
            return ptr
        
    def getEntry(self, pos): # 인덱스 기반 연산
        # 리스트의 pos 위치에 있는 노드를 찾아 데이터값을 반환
        node = self.getNode(pos) # 1. 해당 위치의 노드를 탐색
        if node == None : # 해당 노드가 없는 경우
            return None
        else: # 있는 경우
            return node.data
        
    def insert(self, pos, elem) : # 인덱스 기반 연산 
        # pos 위치에서 새노드(elem) 삽입 연산
        if pos < 0: 
            raise ValueError("잘못된 위치 값!")
        
        new = Node(elem) # 1. 새 노드 생성
        before = self.getNode(pos-1) # 2. pos -1 위치의 노드 탐색
        # 3. before 노드의 위치에 따라 구분
        if before is None :
            if pos == 0: # 1) 머리 노드로 삽입
                new.link = self.head 
                self.head = new 
                return 
            else: # 2) pos가 리스트 범위에서 벗어남
                raise IndexError("삽입할 위치가 유효하지 않음!")
        else:  # 3) 중간 노드로 삽입
            before.append(new)

    def delete(self, pos) : # 인덱스 기반 연산
        # pos 위치에서 해당 노드 삭제한 후 그 노드 반환
        if pos < 0 : 
            raise ValueError("잘못된 위치 값!")
        
        before = self.getNode(pos-1) # 1. 삭제 노드 이전의 노드 탐색
        # 2. before 노드의 위치에 따라 구분
        if before == None :
            if pos == 0: # 1) 머리 노드로 삭제
                deleted = self.head
                self.head = deleted.link
                deleted.link = None # 연결 해제
                return deleted
            else: # 2)pos가 리스트 범위에서 벗어남
                raise IndexError("삽입할 위치가 유효하지 않음!")
        else: # 3) 중간 노드로 삭제
            return before.popNext()
        
    def size(self):
        # 리스트의 전체 노드의 개수
        if self.head == None: # 현재 리스트가 공백이면
            return 0
        else :
            ptr = self.head
            count = 0
            while ptr is not None: 
                count += 1
                ptr = ptr.link
            return count
    
    def display(self, msg = "LinkedList:"):
        # 리스트의 내용을 출력
        print(msg, end = ' ')
        if self.head == None: # 현재 리스트가 공백이면
            return None
        else :
            ptr = self.head
            while ptr is not None: 
                print(ptr.data, end = " -> ")
                ptr = ptr.link
            print('None')

    def replace(self,pos,elem): # 인덱스 기반 연산
        # 리스트의 pos 위치에 있는 노드의 데이터 필드를 수정
        node = self.getNode(pos)
        if node != None: # 해당 노드가 있는 경우
            node.data =  elem   
    
    def find_book(self, title): # 책 제목으로 리스트에서 도서 찾기
        ptr = self.head
        while ptr is not None:
            if ptr.title == title:
                return ptr
            ptr =ptr.next

        return None

    def find_pos_by_title(self, title): # 책 제목으로 리스트에서 도서 위치 찾기 
        ptr=self.head
        pos=0
        while ptr is not None:
            if ptr.title == title:
                return pos
            pos += 1
            ptr = ptr.next

# book 클래스
class Book:
    def __init__(self, number, title, author, year):
        self.number = number      # 책 번호
        self.title = title        # 책 제목
        self.author = author      # 저자
        self.year = year          # 출판 연도
        self.next = None          # 다음 도서를 위한 링크

    def display(self):
        print("책 번호:", self.number)
        print("책 제목:", self.title)
        print("저   자:", self.author)
        print("출판 연도:", self.year)
        print("------------------------")

# bookmanagement 클래스
class bookmanagement:
    def __init__(self):
        self.head = None # 비어 있는 리스트

    def add_book(self, book_id, title, author, year): # 새로운 도서를 추가하는 메서드
        new_book = Book(book_id, title, author, year)

        if self.head is None:      # 리스트가 비었을 경우
            self.head = new_book
            print("새로운 도서가 추가되었습니다.")
            return

    def remove_book(self, title): # 도서를 삭제하는 메서드
        ptr = self.head
        prev = None

        while ptr:
            if ptr.title == title:  # 삭제할 도서 발견
                if prev is None:        # 첫 번째 노드 삭제
                    self.head = ptr.next
                else:                   # 중간 노드 삭제
                    prev.next = ptr.next

                print(f"'{title}' 도서가 삭제되었습니다.")
                return

            prev = ptr
            ptr = ptr.next

        print(f"'{title}' 제목의 도서를 찾을 수 없습니다.")

    def search_book(self, title): # 도서를 검색하는 메서드
        ptr = self.head

        while ptr:
            if ptr.title == title:
                print("[검색 결과]")
                ptr.display()
                return

            ptr = ptr.next

        print(f"'{title}' 제목의 도서는 없습니다.")

    def display_books(self): # 전체 도서를 출력하는 메서드
        if self.head is None:
            print("등록된 도서가 없습니다.")
            return

        print("\n[전체 도서 목록]")
        ptr = self.head
        while ptr:
            ptr.display()
            ptr = ptr.next

    def run(self):
        while True:
            print("\n====== 도서 관리 프로그램 ======")
            print("1. 도서 추가")
            print("2. 도서 삭제")
            print("3. 도서 검색")
            print("4. 전체 도서 출력")
            print("5. 종료")

            choice = input("메뉴 선택: ")

            if choice == "1":
                book_id = int(input("책 번호: "))
                title = input("책 제목: ")
                author = input("저자: ")
                year = int(input("출판 연도: "))
                self.add_book(book_id, title, author, year)

            elif choice == "2":
                title = input("삭제할 책 제목: ")
                self.remove_book(title)

            elif choice == "3":
                title = input("검색할 책 제목: ")
                self.search_book(title)

            elif choice == "4":
                self.display_books()

            elif choice == "5":
                print("프로그램을 종료합니다.")
                break

            else:
                print("[!] 잘못된 입력입니다.")

if __name__ == "__main__":
    bm = bookmanagement()
    bm.run()


