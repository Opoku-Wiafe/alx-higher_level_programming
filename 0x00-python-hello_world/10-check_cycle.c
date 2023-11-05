#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *near, *far;

	near = far = list;

	while (near && far && far->next)
	{
		near = near->next;
		far = far->next->next;
		if (near == far)
			return (1);
	}
	return (0);
}
