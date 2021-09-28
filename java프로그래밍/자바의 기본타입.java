package java프로그래밍;

public class 자바의 기본타입 {
    public static void main(String[]args){
        // 논리타입 boolean (1비트, true 또는 false)
        // 문자타입 char (2비트,Unicode)
        // 정수타입 byte (1바이트. -128~127)
        // 정수타입 short (2바이트 , -32768~32767)
        // 정수타입 int (4바이트 ,2^31~2^31-1) 디폴트
        // 정수타입 long (8바이트 ,2^63~2^63-1)
        // 실수타입 float (4바이트 , -3.4E38~3.4E38)
        // 실수타입 double (8바이트, -1.7E308~1.7E308) 디폴트
        byte b = 127;
        short s = 32767; // 16비트
        int i = 32768; // 32비트(4바이트)
        long l = 9999999999L; // 64비트(8바이트)

        float f = 1.1f;
        double d = 1.1f; // 디폴트

        char c = 'a';

        boolean bool = ture;

}
