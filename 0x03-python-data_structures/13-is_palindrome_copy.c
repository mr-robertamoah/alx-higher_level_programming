#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * add_node - adds a new node at the beginning of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_node(listint_t **head, int n)
{
	listint_t *new;
	listint_t *next;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		next = *head;
		new->next = next;
		(*head) = new;
	}

	return (new);
}

listint_t *reverse_list(listint_t *node)
{
	listint_t *tmp, *next, *prev;

	tmp = NULL;
	while (node != NULL)
	{
		next = node->next;
		if (next)
		{
			prev = tmp;
			tmp = next;
			tmp->next = prev;
		}
		else
			tmp->next = next;
		node = next;
	}
	return (tmp);
}

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
	listint_t *node;
	listint_t *tmp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	node = *head;
	tmp = reverse_list( node);
	while (node != NULL)
	{
		if (tmp->n != node->n)
		{
			return (0);
		}
		tmp = tmp->next;
		node = node->next;
	}
	return (1);
}
