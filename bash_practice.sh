#!/bin/bash

echo "================================="
echo " CloudGuard Bash Practice"
echo " Day 11 - Prajwal CK"
echo "================================="

# VARIABLES
TOOL_NAME="CloudGuard"
VERSION="1.0"
AUTHOR="Prajwal CK"

echo ""
echo "Tool: $TOOL_NAME"
echo "Version: $VERSION"
echo "Author: $AUTHOR"

#IF/ELSE
echo ""
echo "CHECKING SYSTEM..."
if [ "$(whoami)"  == "root" ]; then
    echo "[WARNING] Running as root!"
    echo "          Use normal user instead"
else
    echo "[OK] Running as normal user"
fi

# FOR LOOP
echo ""
echo "CHECKING DANGEROUS PORTS..."
DANGEROUS_PORTS="22 3306 6379 3389"
for PORT in $DANGEROUS_PORTS
do
    echo "Checking port: $PORT"
done

# FUNCTION
check_file() {
    if [  -f "$1" ]; then
        echo "[OK]       $1 exists"
    else
        echo "[MISSING]  $1 not found"
    fi
}

echo ""
echo "CHECKING IMPORTANT FILES..."
check_file "/etc/passwd"
check_file "/etc/ssh/sshd_config"
check_file "/etc/hosts"

# USER INPUT
echo ""
echo "Enter your name:"
read USER_NAME
echo "Welcome $USER_NAME to cloudGuard!"

echo ""
echo "==============================="
echo " Practice Complete"
echo "==============================="