#include <iostream>
using namespace std;
#include <math.h>
class Remocon {
int w, h;
int channel;
int brightness;
int volume;
public:
Remocon() {
w = 30; h = 15;
channel = 19;
brightness = 10;
volume = 50;
}
Remocon(int w, int h, int c = 19 , int b = 10 , int v = 50) {
this->w = w; this->h = h;
channel = c;
brightness = b;
volume = v;
}
int size();
void power(int);
void changechannel(int);
void changebright(int);
void changevol(int);
};
int Remocon::size() {
int s;
s = (int)(sqrt(w * w + h * h) / 2.54);
return s;
}
void Remocon::power(int onoff) {
if (onoff) {
cout << "전원 켜짐" << endl;
cout << "현재 채널:" << channel << endl;
cout << "현재 밝기:" << brightness << endl;
cout << "현재 볼륨:" << volume << endl;
}
else {
cout << "전원 꺼짐" << endl;
}
}
void Remocon::changechannel(int c) {
cout << "채널변경:" << c << endl;
}
void Remocon::changebright(int b) {
cout << "밝기변경:" << b << endl;
}
void Remocon::changevol(int v) {
cout << "볼륨변경:" << v << endl;
}
int main() {
Remocon myTv(52, 29); // cm
int s;
s = myTv.size();
cout << "TV 크기: " << s << "인치" << endl;
myTv.power(1);
myTv.changechannel(10);
myTv.changechannel(30);
myTv.changebright(5);
myTv.changebright(15);
myTv.changevol(25);
myTv.changevol(75);
myTv.power(0);
}