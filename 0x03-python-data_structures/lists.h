
#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>

/**
 * struct listint_s - is a singly linked list
 * @n: is an integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton ALX_higher_level progamming  project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
