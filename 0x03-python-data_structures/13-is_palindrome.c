#include "lists.h"
int is_palindrome(listint_t **head)
{
	listint_t *cur_used = *head, *temp = *head;
	int count = 0, i = 0, j = 0;

	if (!*head)
		return (1);

	while (cur_used)
	{
		cur_used = cur_used->next;
		count++;
	}
	cur_used = *head;
	for (i = 1; i <= count; i++)
	{
		for (j = i; j <= count - i; j++)
			temp = temp->next;
		if (cur_used->n != temp->n)
			return (0);
		cur_used = cur_used->next;
		temp = cur_used;
	}
	return (1);
}
