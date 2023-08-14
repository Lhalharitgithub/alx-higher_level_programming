#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - This printz all elementz of a listint_t list
 * @h: It showz the  pointer to head of list
 * Return: The number of nodez
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
	printf("%i\n", current->n);
	current = current->next;
	n++;
    }

    return (n);
}

/**
 * add_nodeint_end - The function that addz a new node at the end of a listint_t list
 * @head: Showz the pointer to pointer of first node of listint_t list
 * @n: The integer to be included in new node
 * Return: IT address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
	return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
	*head = new;
    else
    {
	while (current->next != NULL)
	    current = current->next;
	current->next = new;
    }

    return (new);
}

/**
 * free_listint - IT showz the freez a listint_t list
 * @head: IT showz pointer to list to be freed
 * Return: The void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
	current = head;
	head = head->next;
	free(current);
    }
}
