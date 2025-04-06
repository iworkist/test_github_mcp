#!/usr/bin/env python
# -*- coding: utf-8 -*-

def hello():
    """Simple function that returns a greeting message"""
    return "Hello, GitHub MCP World!"

def goodbye():
    """Simple function that returns a farewell message"""
    return "Goodbye, GitHub MCP World!"

def main():
    """Main function to print the greeting"""
    message = hello()
    print(message)
    
    # Also print the goodbye message
    farewell = goodbye()
    print(farewell)

if __name__ == "__main__":
    main()
