#include "lists.h"

/**
 * insert_node - This insertz a number into a sorted singly-linked list.
 * @head: Showz the  pointer of the head of the linked list.
 * @number: It is the number to insert.
 *
 * Return: If the function failz - NULL.
 * Otherwise - A pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
