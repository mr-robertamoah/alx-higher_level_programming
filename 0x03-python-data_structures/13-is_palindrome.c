#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* is_palindrome - determine whether or not a linked list
* is palindrome or not
* Return: int (0 or 1)
*/
int is_palindrome(listint_t **head)
{
/**
 * 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 */
	listint_t *slow = *head, *fast = *head;
	int stack[100];
	int top = -1;

	if (fast == NULL)
		return (1);

	while (fast && fast->next)
	{
		stack[++top] = slow->n;
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast)
	{
		slow = slow->next;
	}

	while (slow)
	{
		if (stack[top--] != slow->n)
		{
			return (0);
		}
		slow = slow->next;
	}
	return (1);
}
