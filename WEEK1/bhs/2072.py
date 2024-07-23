- 2072. 홀수만 더하기 D1
    
    문제 링크 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1#
    
    - 코드
    
    import java.util.Scanner;   #스캐너 클래스 사용. 사용자 입력 받는데 사용
    
    public class OddNumberSum {                       
        public static void main(String[] args) {                  #메인 메소드, 진입 시작
            Scanner sc = new Scanner(System.in);             # 객체 생성, 표준 입력
            int T = sc.nextInt();                                            # nextInt()는 int 데스트 케이스 개수 저장.
    
    *// 테스트 케이스의 개수*
    
    for (int t = 1; t <= T; t++) {                                        # 반복
                int sum = 0;                                                    # 저장할 변수 초기화
                for (int i = 0; i < 10; i++) {                               # 10개 반복 
                    int num = sc.nextInt();                                # num에 입력
                    if (num % 2 == 1) {                                    # 홀수인지 아닌지 검사
    
    *// 홀수인 경우*                                          
    
    sum += num;                                                           # 홀수인 경우 더하기
                    }
                }
                System.out.println("#" + t + " " + sum);        # 결과 출력
            }
    
            sc.close();
        }
    }