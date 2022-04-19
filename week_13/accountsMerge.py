class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # construc an email dictionary/ list.
        email_dict = defaultdict(list)
        parents = [idx for idx in range(len(accounts))]

        for account_idx in range(len(accounts)):
            account = accounts[account_idx]
            for idx in range(1, len(account)):
                email_dict[account[idx]].append(account_idx)

        def find(root):
            if root == parents[root]:
                return root
            parents[root] = find(parents[root])
            return parents[root]

        def union(root1, root2):
            parent = find(root1)
            child = find(root2)

            parents[child] = parent

        for email in email_dict:
            names = email_dict[email]
            root1 = names[0]
            for idx in range(1, len(names)):
                root2 = names[idx]
                union(root1, root2)

        users = defaultdict(list)
        for email in email_dict:
            user = find(email_dict[email][0])
            users[user].append(email)

        answer = []
        for user in users:
            emails = users[user]
            emails.sort()
            answer.append([accounts[user][0]] + emails)
        return answer