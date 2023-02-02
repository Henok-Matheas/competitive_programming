class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        given logs
        log
            - letter log(all lowercase except id)
            - digit log(all digits)
            
        reoder them
        letterlogs first
        letterlogs by lexicography(content, id)
        digit logs(maintain relative ordering)
        
        order
        
        letterlogs smallercontent
        letterlogs smallerid
        digitslogs id ->
        
        if it's letterlog(0)
        digitlog(1)
        
        in letterlogs(content, id)
        """
        
        def ordering(value):
            index, log = value
            is_digit = 0
            log_list = log.split()
            id_ = log_list[0]
            content = []
            
            for idx in range(1, len(log_list)):
                word = log_list[idx]
                is_digit |= int(word.isdigit())
                content.append(word)
            
            if is_digit:
                id_, content = "", []
            return (is_digit,content, id_,index)
        
        idx_logs = [(idx, log) for idx, log in enumerate(logs)]
        
        idx_logs.sort(key = lambda value: ordering(value))
        
        new_logs = list(map(lambda value: value[1], idx_logs))
        
        return new_logs