using System.Collections.Generic;
using System;
namespace Test
{
    class ListNode<T>
    {
        public T value { get; set; }
        public ListNode<T> next { get; set; }
    }

    /// <summary>
    /// https://codefights.com/interview/jQyCRiwF2BjBMYy7i
    /// </summary>
    class IsListPalindrome
    {
        private static bool isListPalindrome(ListNode<int> l)
        {
            if (l == null) return true;
            var current = l;
            var next = current.next;
            if (next == null) return true;
            long count = 1;
            List<int> values = new List<int>();
            do
            {
                int currentVal = current.value;
                values.Add(currentVal);
                current = next;
                if (current == null) break;
                next = current.next;
                count++;
            } while (true);

            for(int i = 0, j = (int)count - 1; i < count/2; i++, j--)
            {
                if (values[i] != values[j]) return false;
            }

            return true;
        }

        public static void isListPalindromeMain()
        {
            isListPalindrome(new ListNode<int> {
                value = 1,
                next = new ListNode<int> {
                    value = 0,
                    next = new ListNode<int> { value = 1 }
                }
            });
        }
    }


}
