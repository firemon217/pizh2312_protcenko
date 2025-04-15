#include "number.h"
#include <cstring>
#include <string>
#include <algorithm>

uint2022_t from_uint(uint32_t value) {
    uint2022_t result{};
    result.data[0] = value;
    return result;
}

uint2022_t from_string(const char* str) {
    uint2022_t result{};
    for (const char* p = str; *p; ++p) {
        result = result * from_uint(10);
        result = result + from_uint(*p - '0');
    }
    return result;
}

uint2022_t operator+(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result{};
    uint64_t carry = 0;

    for (size_t i = 0; i < LIMBS; ++i) {
        uint64_t sum = static_cast<uint64_t>(lhs.data[i]) + rhs.data[i] + carry;
        result.data[i] = static_cast<uint32_t>(sum);
        carry = sum >> 32;
    }

    return result;
}

uint2022_t operator-(const uint2022_t& lhs, const uint2022_t& rhs) {
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
    uint2022_t result{};

    for (size_t i = 0; i < LIMBS; ++i) {
        uint64_t carry = 0;
        for (size_t j = 0; j + i < LIMBS; ++j) {
            uint64_t mul = static_cast<uint64_t>(lhs.data[i]) * rhs.data[j];
            uint64_t sum = static_cast<uint64_t>(result.data[i + j]) + mul + carry;
            result.data[i + j] = static_cast<uint32_t>(sum);
            carry = sum >> 32;
        }
    }

    return result;
}

uint2022_t operator/(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result{};
    uint2022_t remainder{};

    for (int i = LIMBS * 32 - 1; i >= 0; --i) {
        for (int j = LIMBS - 1; j > 0; --j) {
            remainder.data[j] <<= 1;
            if (remainder.data[j - 1] & 0x80000000)
                remainder.data[j] |= 1;
        }
        remainder.data[0] <<= 1;

        size_t word = i / 32;
        size_t bit = i % 32;
        if (lhs.data[word] & (1u << bit)) {
            remainder.data[0] |= 1;
        }

        if (!(remainder < rhs)) {
            remainder = remainder - rhs;
            result.data[word] |= (1u << bit);
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

bool operator<(const uint2022_t& lhs, const uint2022_t& rhs) {
    for (int i = LIMBS - 1; i >= 0; --i) {
        if (lhs.data[i] < rhs.data[i]) return true;
        if (lhs.data[i] > rhs.data[i]) return false;
    }
    return false;
}

std::pair<uint2022_t, uint8_t> divmod10(const uint2022_t& value) {
    uint2022_t quotient = from_uint(0);
    uint64_t remainder = 0;

    for (int i = 2; i >= 0; --i) {
        uint64_t part = (remainder << 64) | value.data[i];
        quotient.data[i] = static_cast<uint32_t>(part / 10);
        remainder = part % 10;
    }

    return { quotient, static_cast<uint8_t>(remainder) };
}

std::ostream& operator<<(std::ostream& stream, const uint2022_t& value) {
    if (*reinterpret_cast<const uint64_t*>(value.data) == 0 &&
        *reinterpret_cast<const uint64_t*>(value.data + 1) == 0 &&
        *reinterpret_cast<const uint64_t*>(value.data + 2) == 0) {
        stream << "0";
        return stream;
    }

    uint2022_t temp = value;
    std::string result;

    while (!(temp == from_uint(0))) {
        auto [quotient, remainder] = divmod10(temp);
        result += static_cast<char>('0' + remainder);
        temp = quotient;
    }

    std::reverse(result.begin(), result.end());
    stream << result;
    return stream;
}
