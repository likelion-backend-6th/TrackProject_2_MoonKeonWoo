# TrackProject_MoonKeonWoo
## 도서 대출 웹 서비스(part1)
1. 메인페이지 
    - http://127.0.0.1:8000/
2. 도서 상세 페이지
    - http://127.0.0.1:8000/books/1/
3. 회원 가입
    - http://127.0.0.1:8000/accounts/signup/
4. 로그인
    - http://127.0.0.1:8000/accounts/login/
5. 로그아웃
   - 로그인하면 로그인/회원가입이 로그아웃으로 표시
6. 내 대출 목록
    - http://127.0.0.1:8000/books/my_rentals/
7. 도서 대출
   - 도서 상세 페이지에서 대출 버튼을 클릭하면 내 대출 목록 페이지로 이동
## 도서 대출 웹 서비스(part2)
- [ ] 반납 이메일 알림 (Celery shared_task 활용)
- [x] 도서 리뷰,평점 입력
  - POST /books/<int:book_id>/reviews/
- [ ] 도서 상세 평점 평균 & 리뷰 목록 표시
  - GET /books/<int:book_id>/
- [ ] 사용자 프로필 페이지 (대출수, 평점 평균 리뷰목록)
  - GET /users/<int:user_id>/
### 오류
- [ ] 대출 중복 오류
- [ ] 리뷰 User 로그인한 사용자로 고정 x, 클릭한 Book  
- [x] [no migrations to apply](https://velog.io/@minjeong/pythondjango-no-migrations-to-apply)
### 개선사항
대출 도서 목록(RentalListView)에서 책 저자 출력하기
