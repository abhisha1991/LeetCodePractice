using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    /// <summary>
    /// https://codefights.com/interview-practice/task/gX7NXPBrYThXZuanm/comments
    /// </summary>
    class RemoveKFromList
    {
        public static ListNode<int> removeKFromList(ListNode<int> l, int k)
        {
            ListNode<int> current  = l;
            if (l == null)
            {
                return l;
            }

            // if list starts with k
            bool startsWithK = false;
            while (current != null && current.value == k)
            {
                startsWithK = true;
                current = current.next;
            }
            ListNode<int> effectiveHead = current;
            ListNode<int> prev = current;

            bool foundK = false;
            while (current != null)
            {
                if (current.value == k)
                {
                    foundK = true;
                    current = current.next;
                    continue;
                }

                if (foundK == true)
                {
                    prev.next = current;
                    foundK = false;
                }
                
                if (current.value != k)
                {
                    prev = current;
                }
                current = current.next;

            }

            // If it ends with k
            if (prev.next.value == k)
            {
                prev.next = null;
            }

            switch (startsWithK)
            {
                case false:
                    return l;
                case true:
                    return effectiveHead;
            }
            return null;
        }

        public static void RemoveKFromListMain()
        {
            // removeKFromList(new ListNode<int> { value = 3, next = null }, 3);

            removeKFromList(new ListNode<int> { value = 1, next = new ListNode<int> { value = 3, next = null } }, 3);

            // removeKFromList(new ListNode<int> { value = 1, next = new ListNode<int> { value = 2, next = new ListNode<int> { value = 3, next = new ListNode<int> { value = 4, next = new ListNode<int> { value = 5, next = null } } } } }, 3);

            // removeKFromList(new ListNode<int> { value = 1, next = new ListNode<int> { value = 3, next = new ListNode<int> { value = 3, next = new ListNode<int> { value = 4, next = new ListNode<int> { value = 5, next = null } } } } }, 3);

            // removeKFromList(new ListNode<int> { value = 3, next = new ListNode<int> { value = 3, next = new ListNode<int> { value = 3, next = new ListNode<int> { value = 4, next = new ListNode<int> { value = 5, next = null } } } } }, 3);

            // removeKFromList(new ListNode<int> { value = 3, next = new ListNode<int> { value = 3, next = new ListNode<int> { value = 3, next = new ListNode<int> { value = 3, next = new ListNode<int> { value = 3, next = null } } } } }, 3);

            // removeKFromList(new ListNode<int> { value = 3, next = new ListNode<int> { value = 3, next = new ListNode<int> { value = 3, next = new ListNode<int> { value = 4, next = new ListNode<int> { value = 3, next = new ListNode<int> { value = 5, next = null } } } } } }, 3);
        }

    }
}
