//
// Created by wangwei on 2019/11/23.
//

#include <iostream>
#include "cmath"
using namespace std;

int main(){
    size_t color1 = 0xFEADBC;
    size_t color2 = 0x010000;
    double value1 = 0.0;
    double value2 = 1.0;
    double value = 0.8;
    uint8_t red1 = color1 >> 16 & 0xFF;
    uint8_t green1 = (color1 >> 8) & 0xFF;
    uint8_t blue1 = color1 & 0xFF;
    uint8_t red2 = (color2 >> 16) & 0xFF;
    uint8_t green2 = (color2 >> 8) & 0xFF;
    uint8_t blue2 = color2 & 0xFF;

    double scale = (value - value1) / (value2 - value1);
    auto red_at_value = static_cast<uint8_t>(round((1 - scale) * red1 + scale * red2));
    auto green_at_value = static_cast<uint8_t>(round((1 - scale) * green1 + scale * green2));
    auto blue_at_value = static_cast<uint8_t>(round((1 - scale) * blue1 + scale * blue2));

    auto color_at_value = static_cast<size_t>((red_at_value << 16) + (green_at_value << 8) + blue_at_value);

    printf("RGB1 at value1 %f: %x, %x, %x\n", value1, red1, green1, blue1);
    printf("RGB2 at value2 %f: %x, %x, %x\n", value2, red2, green2, blue2);
    printf("RGB at value %f: %x, %x, %x\n", value, red_at_value, green_at_value, blue_at_value);
    printf("scale: %f\n", double(red_at_value - red1) / (red2 - red1));
    printf("RGB new: %x\n", color_at_value);

    return 0;
}