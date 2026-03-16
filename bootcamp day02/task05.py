class Competition:


    def get_ranking(self):
        ranked = []

       
        for athlete in self.athletes:
            records = athlete.get_records()  

            if self.name in records:
                rank = records[self.name]
                ranked.append((rank, athlete))

        
        if not ranked:
            print(f"The {self.name} has no ranking yet.")
            return

        print(f"The {self.name} rankings are:")

        
        ranked_sorted = sorted(
            ranked,
            key=lambda x: (x[0], x[1].get_name().lower())
        )

        
        for rank, athlete in ranked_sorted:
            print(
                f"Rank {rank}: {athlete.get_name()} from {athlete.get_country()} ({athlete.get_birthdate()})"
            )
