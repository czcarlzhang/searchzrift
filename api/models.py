# from django.db import models
# from django.core.validators import MinValueValidator

# class Summoner(models.Model):
#     # https://developer.riotgames.com/apis#summoner-v4/GET_getBySummonerName
#     summoner_id = models.CharField(max_length=63, unique=True)
#     account_id = models.CharField(max_length=56, unique=True)
#     puuid = models.CharField(max_length=78, unique=True)
#     name = models.CharField(max_length=16)
#     profile_icon_id = models.IntegerField()
#     revision_date = models.IntegerField()
#     summoner_level = models.IntegerField()
#     server = models.CharField(max_length=4)
#     #
#     region = models.CharField(max_length=8)
#     season = models.IntegerField()


# class RankedSoloStat(models.Model):
#     summoner = models.ForeignKey(Summoner, on_delete=models.CASCADE)
#     season = models.IntegerField()
#     # https://developer.riotgames.com/apis#league-v4/GET_getLeagueEntriesForSummoner
#     league_id = models.CharField(max_length=36, blank=True, null=True)
#     tier = models.CharField(max_length=11, blank=True, null=True)
#     rank = models.CharField(max_length=3, blank=True, null=True)
#     league_points = models.IntegerField(blank=True, null=True)
#     wins = models.IntegerField()
#     losses = models.IntegerField()
#     # total stats
#     games_played = models.IntegerField()
#     time_played = models.IntegerField()
#     total_kills = models.IntegerField()
#     total_deaths = models.IntegerField()
#     total_assists = models.IntegerField()
#     total_cs = models.IntegerField()
#     total_rating = models.FloatField(validators=[MinValueValidator(0)])


# class ChampionStat(models.Model):
#     summoner = models.ForeignKey(Summoner, on_delete=models.CASCADE)
#     season = models.IntegerField()
#     champion_name = models.CharField(max_length=16) # change number
#     # total stats
#     games_played = models.IntegerField()
#     wins = models.IntegerField()
#     losses = models.IntegerField()
#     time_played = models.IntegerField()
#     total_kills = models.IntegerField()
#     total_deaths = models.IntegerField()
#     total_assists = models.IntegerField()
#     total_cs = models.IntegerField()
#     total_rating = models.FloatField(validators=[MinValueValidator(0)])

# class MatchStat(models.Model):
#     summoner = models.ForeignKey(Summoner, on_delete=models.CASCADE)
#     season = models.IntegerField()
#     match_id = models.CharField(max_length=20)
#     # https://developer.riotgames.com/apis#match-v5/GET_getMatch
#     game_creation = models.IntegerField()
#     game_duration = models.IntegerField()
#     game_start_time_stamp = models.IntegerField()
#     game_end_time_stamp = models.IntegerField()
#     game_version = models.CharField(max_length=20)
#     platform_id = models.CharField(max_length=4)
#     # queue_id = 420 (RANKED_SOLO_5x5)
#     queue_id = models.IntegerField()
#     # team stats
#     ally_baron_kills = models.IntegerField()
#     ally_champion_kills = models.IntegerField()
#     ally_dragon_kills = models.IntegerField()
#     ally_inhibitor_kills = models.IntegerField()
#     ally_rift_herald_kills = models.IntegerField()
#     ally_tower_kills = models.IntegerField()
#     enemy_baron_kills = models.IntegerField()
#     enemy_champion_kills = models.IntegerField()
#     enemy_dragon_kills = models.IntegerField()
#     enemy_inhibitor_kills = models.IntegerField()
#     enemy_rift_herald_kills = models.IntegerField()
#     enemy_tower_kills = models.IntegerField()
#     # stats
#     assists = models.IntegerField()
#     baron_kills = models.IntegerField()
#     bounty_level = models.IntegerField()                                            
#     champ_experience = models.IntegerField()
#     champ_level = models.IntegerField()
#     champion_id = models.IntegerField()
#     champion_name = models.CharField(max_length=20)
#     champion_transform = models.IntegerField()                                      # kayn only (Legal values: 0 - None, 1 - Slayer, 2 - Assassin)
#     consumables_purchased = models.IntegerField()
#     damage_dealt_to_builldings = models.IntegerField()
#     damage_dealt_to_objectvies = models.IntegerField()
#     damage_dealt_to_turrets = models.IntegerField()
#     damage_self_mitigated = models.IntegerField()
#     deaths = models.IntegerField()
#     detector_wards_placed = models.IntegerField()
#     double_kills = models.IntegerField()
#     dragon_kills = models.IntegerField()
#     first_blood_assist = models.BooleanField()
#     first_blood_kill = models.BooleanField()
#     first_tower_assist = models.BooleanField()
#     first_tower_kill = models.BooleanField()
#     game_ended_in_early_surrender = models.BooleanField()
#     game_ended_in_surrender = models.BooleanField()
#     gold_earned = models.IntegerField()                                             
#     gold_spent = models.IntegerField()                         
#     individual_position = models.CharField(max_length=16)                                        
#     inhibitor_kills = models.IntegerField()
#     inhibitor_takedowns = models.IntegerField()
#     inhibitors_lost = models.IntegerField()
#     item0 = models.IntegerField()
#     item1 = models.IntegerField()
#     item2 = models.IntegerField()
#     item3 = models.IntegerField()
#     item4 = models.IntegerField()
#     item5 = models.IntegerField()
#     item6 = models.IntegerField()
#     items_purchased = models.IntegerField()
#     killing_sprees = models.IntegerField()
#     kills = models.IntegerField()
#     lane = models.CharField(max_length=16)
#     largest_critical_strike = models.IntegerField()
#     largest_killing_spree = models.IntegerField()                                   
#     largest_multi_kill = models.IntegerField()                                      
#     longest_time_spent_living = models.IntegerField()                               
#     magic_damage_dealt = models.IntegerField()                                      
#     magic_damage_dealt_to_champions = models.IntegerField()                         
#     magic_damage_taken = models.IntegerField()                                      
#     neutral_minions_killed = models.IntegerField()
#     nexus_kills = models.IntegerField()
#     nexus_lost = models.IntegerField()
#     nexus_takedowns = models.IntegerField()
#     objectives_stolen = models.IntegerField()
#     objectives_stolen_assists = models.IntegerField()
#     participant_id = models.IntegerField()       
#     penta_kills = models.IntegerField()                                             
#     physical_damage_dealt = models.IntegerField()                                   
#     physical_damage_dealt_to_champions = models.IntegerField()                      
#     physical_damage_taken = models.IntegerField()                                   
#     profile_icon = models.IntegerField()
#     puuid = models.CharField(max_length=78)
#     quadra_kills = models.IntegerField()                                           
#     riot_id_name = models.CharField(blank=True, max_length=16)
#     riot_tag_line = models.CharField(blank=True, max_length=16)
#     role = models.CharField(max_length=16)                               
#     sight_wards_bought_in_game = models.IntegerField()                 
#     spell1_casts = models.IntegerField()
#     spell2_casts = models.IntegerField()
#     spell3_casts = models.IntegerField()
#     spell4_casts = models.IntegerField()
#     summoner1_casts = models.IntegerField()
#     summoner1_id = models.IntegerField()
#     summoner2_casts = models.IntegerField()
#     summoner2_id = models.IntegerField()
#     summoner_level = models.IntegerField()
#     team_early_surrender = models.BooleanField()
#     team_id = models.IntegerField()
#     team_position = models.CharField(blank=True, max_length=16)
#     time_ccing_others = models.IntegerField()                                       
#     time_played = models.IntegerField()                                             
#     total_damage_dealt = models.IntegerField()                                      
#     total_damage_dealt_to_champions = models.IntegerField()                         
#     total_damage_shielded_on_teammates = models.IntegerField()                      
#     total_damage_taken = models.IntegerField()                                      
#     total_heal = models.IntegerField()                                              
#     total_heals_on_teammates = models.IntegerField()                                
#     total_minions_killed = models.IntegerField()                                    
#     total_time_cc_dealt = models.IntegerField()                                     
#     total_time_spent_dead = models.IntegerField()                                   
#     total_units_healed = models.IntegerField()                                      
#     triple_kills = models.IntegerField()                                            
#     true_damage_dealt = models.IntegerField()                                       
#     true_damage_dealt_to_champions = models.IntegerField()                          
#     true_damage_taken = models.IntegerField()                                       
#     turret_kills = models.IntegerField()
#     turret_takedowns = models.IntegerField()
#     turrets_lost = models.IntegerField()
#     unreal_kills = models.IntegerField()
#     vision_score = models.IntegerField()                                            
#     vision_wards_bought_in_game = models.IntegerField()                             
#     wards_killed = models.IntegerField()                                            
#     wards_placed = models.IntegerField()                                            
#     win = models.BooleanField()
#     #
#     match_rating = models.FloatField(validators=[MinValueValidator(0)])
