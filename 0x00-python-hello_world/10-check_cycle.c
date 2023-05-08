#include "lists.h"

/**
 * check_cycle - check if there is a cycle
 * @list: pointer to list's head
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;

	if (!list)
		return (0);

	hare = list;
	tortoise = list;

	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		tortoise = tortoise->next;

		if (hare == tortoise)
			return (1);
	}

	return (0);
}
