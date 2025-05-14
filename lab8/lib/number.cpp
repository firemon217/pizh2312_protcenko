#include "number.h"
#include <string>
#include <cstring>
#include <stdexcept>
#include <algorithm>

using namespace std;

int chuse() {
    setlocale(LC_ALL, "Russian");
    int chuse = 0;
    cout << "Выберите: число будет обрезаться(1), число любой длинны(2):";
    cin >> chuse;
    return chuse;
}

bool operator<(const uint2022_t& lhs, const uint2022_t& rhs) {
    for (int i = LIMBS - 1; i >= 0; --i) {
        if (lhs.data[i] < rhs.data[i]) return true;
        if (lhs.data[i] > rhs.data[i]) return false;
    }
    return false;
}

bool operator>(const uint2022_t& lhs, const uint2022_t& rhs) {
    return rhs < lhs;
}

uint2022_t from_uint(uint32_t i) {
    uint2022_t result{};
    result.data[0] = i;
    return result;
}

uint2022_t from_string(const char* buff) {
    uint2022_t result = from_uint(0);
    string str(buff);
    int cnt = 1;

    for (char ch : str) {
        if (!isdigit(ch)) {
            throw invalid_argument("Invalid digit in string");
        }
        result = result * from_uint(10);
        result = result + from_uint(ch - '0');
        cnt++;
    }

    return result;
}

uint2022_t operator+(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result{};
    uint64_t carry = 0;

    const auto MAX_70_DIGIT = [] {
        uint2022_t value = from_uint(1);
        for (int i = 0; i < 70; ++i) {
            value = value * from_uint(10);
        }
        return value;
        }();

    if (lhs > MAX_70_DIGIT || rhs > MAX_70_DIGIT || MAX_70_DIGIT - lhs < rhs) {
        throw overflow_error("Overflow in uint2022_t addition");
    }

    for (size_t i = 0; i < LIMBS; ++i) {
        uint64_t sum = static_cast<uint64_t>(lhs.data[i]) + rhs.data[i] + carry;
        result.data[i] = static_cast<uint32_t>(sum);
        carry = sum >> 32;
    }

    if (carry || result > MAX_70_DIGIT) {
        throw overflow_error("Overflow in uint2022_t addition");
    }

    return result;
}

uint2022_t operator-(const uint2022_t& lhs, const uint2022_t& rhs) {
    if (lhs < rhs) {
        throw overflow_error("Overflow in uint2022_t subtraction");
    }

    uint2022_t result{};
    int64_t borrow = 0;

    for (size_t i = 0; i < LIMBS; ++i) {
        int64_t diff = static_cast<int64_t>(lhs.data[i]) - rhs.data[i] - borrow;
        if (diff < 0) {
            diff += (1LL << 32);
            borrow = 1;
        }
        else {
            borrow = 0;
        }
        result.data[i] = static_cast<uint32_t>(diff);
    }

    return result;
}

uint2022_t operator*(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint64_t temp[2 * LIMBS]{};
    bool nonZeroLhs = false, nonZeroRhs = false;

    for (size_t i = 0; i < LIMBS; ++i) {
        nonZeroLhs |= lhs.data[i] != 0;
        nonZeroRhs |= rhs.data[i] != 0;
    }

    for (size_t i = 0; i < LIMBS; ++i) {
        uint64_t carry = 0;
        for (size_t j = 0; j < LIMBS; ++j) {
            size_t k = i + j;
            if (k >= 2 * LIMBS) continue;
            uint64_t mul = static_cast<uint64_t>(lhs.data[i]) * rhs.data[j];
            uint64_t sum = temp[k] + mul + carry;
            temp[k] = static_cast<uint32_t>(sum);
            carry = sum >> 32;
        }
        if (i + LIMBS < 2 * LIMBS) {
            temp[i + LIMBS] += carry;
        }
        else if (carry != 0) {
            cerr << "Overflow in uint2022_t multiplication" << endl;
            throw overflow_error("Overflow");
        }
    }

    for (size_t i = LIMBS; i < 2 * LIMBS; ++i) {
        if (temp[i] != 0) {
            cerr << "Overflow in uint2022_t multiplication" << endl;
            throw overflow_error("Overflow");
        }
    }

    uint2022_t result{};
    for (size_t i = 0; i < LIMBS; ++i) {
        result.data[i] = static_cast<uint32_t>(temp[i]);
    }

    if (result == from_uint(0) && nonZeroLhs && nonZeroRhs) {
        cerr << "Unexpected zero result in multiplication" << endl;
        throw overflow_error("Unexpected zero in multiplication");
    }

    return result;
}

uint2022_t operator/(const uint2022_t& lhs, const uint2022_t& rhs) {
    if (rhs == from_uint(0)) {
        throw domain_error("Division by zero");
    }

    uint2022_t result = from_uint(0);
    uint2022_t remainder = from_uint(0);

    for (int i = LIMBS * 32 - 1; i >= 0; --i) {
        for (int j = LIMBS - 1; j > 0; --j) {
            remainder.data[j] = (remainder.data[j] << 1) | (remainder.data[j - 1] >> 31);
        }
        remainder.data[0] = (remainder.data[0] << 1) | ((lhs.data[i / 32] >> (i % 32)) & 1);
        if (!(remainder < rhs)) {
            remainder = remainder - rhs;
            result.data[i / 32] |= (1u << (i % 32));
        }
    }

    return result;
}

bool operator==(const uint2022_t& lhs, const uint2022_t& rhs) {
    for (size_t i = 0; i < LIMBS; ++i) {
        if (lhs.data[i] != rhs.data[i]) return false;
    }
    return true;
}

bool operator!=(const uint2022_t& lhs, const uint2022_t& rhs) {
    return !(lhs == rhs);
}

pair<uint2022_t, uint8_t> divmod10(const uint2022_t& value) {
    uint2022_t quotient = from_uint(0);
    uint64_t remainder = 0;

    for (int i = LIMBS - 1; i >= 0; --i) {
        uint64_t part = (remainder << 32) | value.data[i];
        quotient.data[i] = static_cast<uint32_t>(part / 10);
        remainder = part % 10;
    }

    return { quotient, static_cast<uint8_t>(remainder) };
}

ostream& operator<<(ostream& stream, const uint2022_t& value) {
    uint2022_t temp = value;
    string digits;

    while (!(temp == from_uint(0))) {
        auto [quotient, remainder] = divmod10(temp);
        digits.push_back(static_cast<char>('0' + remainder));
        temp = quotient;
    }

    if (digits.empty()) digits = "0";
    std::reverse(digits.begin(), digits.end());

    stream << digits;
    return stream;
}
