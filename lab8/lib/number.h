#pragma once
#include <cinttypes>
#include <iostream>

const size_t LIMBS = 70;

struct uint2022_t {
    uint32_t data[LIMBS]{};
};

static_assert(sizeof(uint2022_t) <= 300, "");

uint2022_t from_uint(uint32_t value);
uint2022_t from_string(const char* str);

uint2022_t operator+(const uint2022_t& lhs, const uint2022_t& rhs);
uint2022_t operator-(const uint2022_t& lhs, const uint2022_t& rhs);
uint2022_t operator*(const uint2022_t& lhs, const uint2022_t& rhs);
uint2022_t operator/(const uint2022_t& lhs, const uint2022_t& rhs);

bool operator==(const uint2022_t& lhs, const uint2022_t& rhs);
bool operator!=(const uint2022_t& lhs, const uint2022_t& rhs);
bool operator<(const uint2022_t& lhs, const uint2022_t& rhs);

std::ostream& operator<<(std::ostream& stream, const uint2022_t& value);
