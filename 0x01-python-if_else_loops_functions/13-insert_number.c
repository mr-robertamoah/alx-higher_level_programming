#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert node
 * @head: pointer to a pointer of the start of the list
 * @number: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *nextnode;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
		while (current != NULL)
		{
			nextnode = current->next;

			if (current->n >= number)
			{
				*head = new;
				new->next = current;
				break;
			}
			if (
				(current->n < number && nextnode && nextnode->n >= number) ||
				!nextnode
			)
			{
				current->next = new;
				if (nextnode)
					current->next->next = nextnode;
				break;
			}
			current = current->next;
		}
	}

	return (new);
}
