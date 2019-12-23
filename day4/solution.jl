function valid_password1(password)
    has_duplicate = false
    str_pass = string(password)
    val = parse(Int, str_pass[1])
    for char = str_pass[2:length(str_pass)]
        new_val = parse(Int, char)
        if (!has_duplicate) & (val == new_val)
            has_duplicate = true
        end
        if new_val < val
            return false
        end
        val = new_val
    end
    return has_duplicate
end

function valid_password2(password)
    str_pass = string(password)
    val1 = parse(Int, str_pass[1])
    val2 = parse(Int, str_pass[2])
    val3 = parse(Int, str_pass[3])
    val4 = parse(Int, str_pass[4])
    if (val2 < val1) | (val3 < val2) | (val4 < val3)
        return false
    elseif ((val1 == val2) & (val2 != val3))
        has_duplicate = true
    elseif ((val2 == val3) & (val3 != val4) & (val1 != val2))
        has_duplicate = true
    else
        has_duplicate = false
    end

    for char = str_pass[5:length(str_pass)]
        val1 = val2
        val2 = val3
        val3 = val4
        val4 = parse(Int, char)
        if val4 < val3
            return false
        elseif ((val2 == val3) & (val3 != val4) & (val1 != val2))
            has_duplicate = true
        end

    end
    return has_duplicate | ((val3 == val4) & (val2 != val3))
end

function crack_password(lower, upper, valid_test)
    test_password = lower
    valid_count = 0
    for test_password = lower:upper
        if valid_test(test_password)
            println(test_password)
            valid_count +=1
        end
    end
    return valid_count
end

# Part 1
pwd = crack_password(146810, 612564, valid_password1)
println(pwd)

# Part 2
@assert valid_password2(112233) == true
@assert valid_password2(123444) == false
@assert valid_password2(111122) == true

pwd = crack_password(146810, 612564, valid_password2)
println(pwd)
